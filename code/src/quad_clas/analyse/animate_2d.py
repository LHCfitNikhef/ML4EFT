def animate_learning_2d(path, network_size, train_dataset, quadratic, ctg, cuu, epochs):
    # stopping_point = int(glob.glob(path + "/trained_nn_*.pt", recursive=False)[0][-6:-3])
    # print(stopping_point)
    # sys.exit()

    with open(path + 'stopping.txt') as f:
        stopping_point = int(f.read())

    def reference():
        mtt_min, mtt_max = 1000.0, 4000.0
        s = (14 * 10 ** 3) ** 2
        reference.y_min, reference.y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
        x_spacing = 10
        y_spacing = 0.01
        # First set up the figure, the axis, and the plot element we want to animate
        reference.f_ana = axs.plot_f_ana(mtt_min, mtt_max, reference.y_min, reference.y_max, x_spacing, y_spacing, ctg,
                                         cuu, np_order=2)
        reference.f_ana = np.ma.masked_where(reference.f_ana == 1.0, reference.f_ana)

    reference()

    cmap = copy.copy(plt.get_cmap("seismic"))
    cmap.set_bad(color='#c8c9cc')

    fig, ax = plt.subplots()
    img = plt.imshow(np.zeros(reference.f_ana.shape), extent=[1000.0, 4000.0, reference.y_min, reference.y_max],
                     origin='lower', cmap=cmap, aspect=(4000.0 - 1000.0) / (reference.y_max - reference.y_min),
                     interpolation='quadric', vmin=0.8, vmax=1.2)
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('Rapidity y')
    plt.title('NN performance at ctG = {}'.format(ctg))
    epoch_text = ax.text(0.70, 0.95, '', transform=ax.transAxes)
    loss_text = ax.text(0.70, 0.90, '', transform=ax.transAxes)
    loss = np.loadtxt(path + 'loss.out')

    # initialization function: plot the background of each frame
    def init():
        img.set_data(np.zeros(reference.f_ana.shape))
        epoch_text.set_text('')
        loss_text.set_text('')
        return img, epoch_text, loss_text

    # animation function.  This is called sequentially

    def animate(i):
        sys.stdout.write('\r')
        sys.stdout.flush()
        xx, yy, _, _, f_pred, n_alpha_nn, n_alpha_n_beta_nn = make_predictions_2d(
            path + 'trained_nn_{}.pt'.format(i + 1), network_size, train_dataset, quadratic, ctg, make_animation=True)
        img.set_array(reference.f_ana / f_pred)
        epoch_text.set_text('epoch = {}'.format(i))
        loss_text.set_text('loss = {:.4f}'.format(loss[i]))
        return img, epoch_text, loss_text

    # call the animator.  blit=True means only re-draw the parts that have changed.
    print("Creating the animation")
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=stopping_point, interval=200, blit=True)
    anim.save(path + 'animation/training_animation.gif')

